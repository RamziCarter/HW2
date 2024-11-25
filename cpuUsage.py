from flask import Flask, jsonify
import psutil

application = Flask(__name__)

@application.route('/', methods=['GET'])
def home():
    return "<h1>Ramzi's Computer System Usage API</h1><p>Paste Endpoints:</p><ul><li>cpu: /CurrentCPU_Usage</li><li>mem: /memory_usage</li><li>disk: /disk_usage</li><li>bandwidth: /bandwidth_usage</li></ul>"


@application.route('/CurrentCPU_Usage', methods=['GET'])
def cpuUsage():
    CurrentCPU_Usage = psutil.cpu_percent(interval=1)
    info = {
        "CurrentCPU_Usage": CurrentCPU_Usage,
        "CPUStatus": "busyCPU" if CurrentCPU_Usage > 75 else "notBusyCPU"
    }
    return jsonify(info)


@application.route('/memory_usage', methods=['GET'])
def memUsage():
    memInfo = psutil.virtual_memory()
    info = {
        "TotalMemory": memInfo.total / (1024 ** 3),  #-->
        "UsedMemory": memInfo.used / (1024 ** 3),    #-->
        "FreeMemory": memInfo.free / (1024 ** 3),    #GBconversion
        "MemoryUsagePercentage": memInfo.percent
    }
    return jsonify(info)


@application.route('/disk_usage', methods=['GET'])
def disk_Usage():
    diskInfo = psutil.disk_usage('/')
    info = {
        "TotalDiskSpace": diskInfo.total / (1024 ** 3),  #--> 
        "UsedDiskSpace": diskInfo.used / (1024 ** 3),    #-->
        "FreeDiskSpace": diskInfo.free / (1024 ** 3),    # GBconversion
        "DiskUsagePercentage": diskInfo.percent
    }
    return jsonify(info)

@application.route('/bandwidth_usage', methods=['GET'])
def bandwidth_Usage():
    internetInfo = psutil.net_io_counters()
    info = {
        "TotalBandwidthUsed": internetInfo.bytes_sent + internetInfo.bytes_recv / (1024 ** 3),  #-->
    }
    return jsonify(info)

if __name__ == '__main__':
    application.run(debug=True)

