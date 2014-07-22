# Alpha O. Sall
# 07/2014

from flask import Flask, request, Response
import json
import requests
from array import *
import salt.client
local = salt.client.LocalClient()

def pool_manage_salt(id, minion):
    if request.method == 'GET':
        if id == None:

            my_cmd = local.cmd(minion,'cmd.run',['ceph osd lspools --format=json'])
            list_pools = json.loads(my_cmd[minion])
          
            skeleton = {'status':'OK','output':[]}
            for i in list_pools:
                skeleton['output'].append(i) 
            result = json.dumps(skeleton)        
            return Response(result, mimetype='application/json')  

        else:
            
            cmd = local.cmd(minion,'cmd.run',['ceph osd dump --format=json'])
            result = json.loads(cmd[minion])
            pools = result['pools']
            for i in range(len(pools)):
                if id = pools[i]['pool']:
                    r = json.dumps(pools[i])
                    return Response(r, mimetype='application/json')
                else:
                    return 'Pool id not found'
