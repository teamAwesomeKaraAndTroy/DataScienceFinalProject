import requests
import sys
import json
import os

if __name__ == '__main__':

    tfile_name = './mesowest/token.json'

    tfile = open(tfile_name)

    obj = json.loads(tfile.read())

    token = obj['TOKEN']

    if len(sys.argv) == 1:
        print('You must provide the station id')
    else:
        request_string = 'https://api.mesowest.net/v2/stations/metadata?stid='
        request_string += sys.argv[1]
        request_string += '&complete=1'
        request_string += '&token=' + token

        r = requests.get(request_string)

        obj = json.loads(r.text)

        station_array = obj['STATION']
        station_obj = station_array[0]
        county = station_obj['COUNTY']

        if county not in os.listdir('./mesowest/'):
            os.mkdir('./mesowest/' + county)

        outfile_name = './mesowest/' + county + '/' + sys.argv[1] + '_metadata.json'

        outfile = open(outfile_name, 'w')

        outfile.write(r.text)

        outfile.close()
        tfile.close()


