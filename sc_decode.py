"""
Tool to extract data from Clash Royale's .sc files.
More info here: https://github.com/umop-aplsdn/sc_decode/wiki

"""

import argparse
import binascii
import struct

def data_dump_to_hex(filein,  fileout):
    print('processing {}'.format(filein))
    with open(filein,  'rb') as fin,  open(fileout,  'w') as fout:
        i = 0
        data = fin.read()
        #read header: number of blocks
        totalsprites,   = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        totalanims,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        totalsheets,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        totaltexts,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        totaltransfs,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        totalcolortrans,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 7 #add 5 '00' bytes
        totalstrings,  = struct.unpack('<H',  bytes(data[i:i+2]))
        i += 2
        
        #strings
        stringlist = [[0 for y in range (2)] for x in range(totalstrings)]
        for x in range (totalstrings):
            stringlist[x][0],  = struct.unpack('<H',  bytes(data[i:i+2]))
            i += 2
        for x in range(totalstrings):            
            stringlen,  = struct.unpack('<B',  bytes(data[i:i+1]))
            i += 1
            stringlist[x][1],  = struct.unpack(str(stringlen) + 's',  bytes(data[i:i+stringlen]))
            i += stringlen       
        print('Total strings: {}'.format(totalstrings),  file=fout)
        maxrange = len(str(totalstrings))
        for x in range(totalstrings):
            
            print('{}:{};{}'.format(str(x).rjust(maxrange,  '0'), format(stringlist[x][0],  'x'),  stringlist[x][1].decode()),  file=fout)
        print(file=fout)
        
        #0x17 and 0x1A blocks (empty)
        tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
        if  (tmpvar  == 0x17):
            print ('17 block present',  file=fout)
            i += 5
        tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
        if (tmpvar  == 0x1A):
            print ('1A block present',  file=fout)
            i += 5
        print(file=fout)
        
        #sprite sheet blocks, either 0x01 or 0x18
        print('Total sprite sheets: {}'.format(totalsheets),  file=fout)
        maxrange = len(str(totalsheets))
        for x in range(totalsheets):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x01 or tmpvar == 0x18):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be either 0x01 or 0x18, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)
        
        #sprite blocks, 0x12
        print('Total sprites: {}'.format(totalsprites),  file=fout)
        maxrange = len(str(totalsprites))
        for x in range(totalsprites):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x12):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be 0x12, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)
        
        #text blocks: 0x19, 0x07, 0x0F
        print('Total text blocks: {}'.format(totaltexts),  file=fout)
        maxrange = len(str(totaltexts))
        for x in range(totaltexts):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x19 or tmpvar == 0x07 or tmpvar == 0x0F):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be either 0x19, 0x07 or 0x0F, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)
        
        
        #transform matrices 0x08
        print('Total transformation matrices: {}'.format(totaltransfs),  file=fout)
        maxrange = len(str(totaltransfs))
        for x in range(totaltransfs):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x08):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be 0x08, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)
        
        #color transforms 0x09
        print('Total color transforms: {}'.format(totalcolortrans),  file=fout)
        maxrange = len(str(totalcolortrans))
        for x in range(totalcolortrans):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x09):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be 0x09, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)
        #animations 0x0C
        print('Total animations: {}'.format(totalanims),  file=fout)
        maxrange = len(str(totalanims))
        for x in range(totalanims):
            tmpvar,  = struct.unpack('<B',  bytes(data[i:i+1]))
            if (tmpvar == 0x0C):
                i += 1
                blocklen,  = struct.unpack('<I',  bytes(data[i:i+4]))
                i += 4
                blockdata,  = struct.unpack(str(blocklen) + 's',  bytes(data[i:i+blocklen]))
                print('{}:{}'.format(str(x).rjust(maxrange,  '0'),  binascii.hexlify(blockdata).decode()),  file=fout)
                i += blocklen
            else:
                print('strange, this byte should be 0x0C, but I got {} at position {}'.format(tmpvar,  i))
                return
        print(file=fout)



if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description = 'Extract data from Clash Royale sprite files')
    parser.add_argument('-d',  action = 'store_true' , help='dumps the data in hex to a file')
    #parser.add_argument('-dd',  help='dumps the structured data in hex to a given file',  nargs='?',  const ='nofile')
    #parser.add_argument('-s', action = 'store_true',  help='extracts all sprites from a file (requires extracted PNG(s) in the same folder')
    parser.add_argument('files', help='extracted sc file', nargs=1)

    args = parser.parse_args()
    #TO-DO: check if files are in .sc, warn user that the file should be extracted first

    if args.d:
        for x in range(args.files):
            fileout = args.files[x] + '_dump.txt'
            data_dump_to_hex(args.files[x],  fileout)
    
    
