from PIL import Image, ImageDraw
images = ['charged','positive','negative','polar','hydrophobic','lysine','arginine','aspartate','glutamate','serine','threonine','tyrosine','cysteine',
          'asparagine','glutamine','histidine','glycine','alanine','valine','phenylalanine','tryptophan','leucine','isoleucine','methionine','proline']
image = 0
categories = [['K','R','D','E'],                    ## charged
              ['K','R'],                            ## positive
              ['D','E'],                            ## negative
              ['S','T','Y','C','N','Q','H','G'],    ## polar
              ['A','V','F','W','L','I','M','P'],    ## hydrophobic
              ['K'],['R'],['D'],['E'],['S'],['T'],['Y'],['C'],['N'],['Q'],['H'],['G'],['A'],['V'],['F'],['W'],['L'],['I'],['M'],['P']]

protLength = 765    ##insert protein length here

for entry in images:
    residue = 0
    newImage = Image.new('RGBA', (protLength,50), (210,234,233))
    img_draw = ImageDraw.Draw(newImage)
    file = open("protein.txt","r")
    for line in file:
        for char in line:
            if char != '\n':
                for letter in categories[image]:
                    if char == letter:
                        img_draw.line(((residue,0),(residue,49)),(219,58,65),1)
                residue += 1
    newImage.save(entry + '.png')
    image += 1
