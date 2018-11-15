import requests
import json
import sys


if __name__ == '__main__':
    
    
    if len(sys.argv) < 6:
        print('You must provide the following arguments to your data request')
        print('arg1: <query_type> one of "timeseries", "climatology", or "statistics"')
        print('arg2: <stid> the id of the station to pull data from')
        print('arg3: <start_date> the start date, formatted YYYYMMDDHHMM')
        print('arg4: <end_date> the end date, formatted YYYYMMDDHHMM')
        print('arg5: <out_folder> the folder in which the data .json file will be written')

    else:
        tfile_name = './mesowest/token.json'

        tfile = open(tfile_name)

        json_string = tfile.read()

        token_dict = json.loads(json_string)

        token_string = token_dict['TOKEN']

        query_type = sys.argv[1] # must be one of 'timeseries', 'climatology', or 'statistics'
        stid = sys.argv[2]
        start = sys.argv[3]
        end = sys.argv[4]
        outfolder = sys.argv[5]

        request_string = 'http://api.mesowest.net/v2/stations/' + query_type
        request_string += '?stid=' + stid
        
        if query_type == 'statistics':
            request_string += '&type=all'

        if query_type == 'climatology':
            request_string += '&startclim=' + start
            request_string += '&endcliim=' + start
        else:
            request_string += '&start=' + start
            request_string += '&end=' + end
        
        request_string += '&token=' + token_string

        r = requests.get(request_string)

        outfile_name = stid + '_' + query_type + '_' + start + '_' + end + '.json'
        outfile_name = './mesowest/' + outfolder + '/' + outfile_name

        outfile = open(outfile_name, 'w')

        outfile.write(r.text)

        tfile.close()
        outfile.close()






