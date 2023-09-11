# iperf3

rocky 8.6 iperf3 解析

```
Something I hope you know before go into the coding~
First, please watch or star this repo, I'll be more happy if you follow me.
Bug report, questions and discussion are welcome, you can post an issue or pull a request.
```

```
Name         : iperf3
Version      : 3.5
Release      : 7.el8_8
Architecture : x86_64
Size         : 229 k
Source       : iperf3-3.5-7.el8_8.src.rpm
Repository   : @System
From repo    : appstream
Summary      : Measurement tool for TCP/UDP bandwidth performance
URL          : http://github.com/esnet/iperf
License      : BSD
Description  : Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
             : various parameters and UDP characteristics. Iperf reports bandwidth, delay
             : jitter, data-gram loss.
File list    :
    /usr/bin/iperf3
    /usr/lib/.build-id
    /usr/lib/.build-id/7d
    /usr/lib/.build-id/7d/44049b04b16a3f636393f7410d4f4d0377de61
    /usr/lib/.build-id/e4
    /usr/lib/.build-id/e4/1daa7717445608bb2a11a13818596e7dd313bf
    /usr/lib64/libiperf.so.0
    /usr/lib64/libiperf.so.0.0.0
    /usr/share/doc/iperf3
    /usr/share/doc/iperf3/LICENSE
    /usr/share/doc/iperf3/README.md
    /usr/share/doc/iperf3/RELNOTES.md
    /usr/share/man/man1/iperf3.1.gz
    /usr/share/man/man3/libiperf.3.gz
```

## 基本使用

iperf3是一个用于测量IP网络上最大可用带宽的工具，它支持TCP，UDP和SCTP协议，以及IPv4和IPv6地址。
iperf3是一个客户端/服务器模式的程序，需要在两台主机上分别运行客户端和服务器端。

服务端执行下列命令，监听5201端口等待客户端的连接。

```shell
iperf3 -s
```

客户端执行下列命令，默认10秒的TCP带宽测试，并报告测试结果。

```shell
iperf3 -c <服务器IP地址>
```

可以使用不同的参数来调整iperf3的测试选项，例如：

* -t <秒数>：指定测试持续的时间，例如```iperf3 -c <服务器IP地址> -t 60```表示进行60秒的测试。
* -i <秒数>：指定报告间隔的时间，例如```iperf3 -c <服务器IP地址> -i 5```表示每5秒报告一次测试结果。
* -b <带宽>：指定目标带宽，例如```iperf3 -c <服务器IP地址> -u -b 100M```表示使用UDP协议并限制带宽为100 Mbps。
* -R：指定反向模式，即从服务器端向客户端发送数据，例如```iperf3 -c <服务器IP地址> -R```。 
* -P <数量>：指定并行流的数量，例如```iperf3 -c <服务器IP地址> -P 4```表示使用4个并行流进行测试。
* -w <大小>：指定TCP窗口大小，例如```iperf3 -c <服务器IP地址> -w 1M```表示设置TCP窗口大小为1 MB。
* -l <大小>：指定数据包大小，例如```iperf3 -c <服务器IP地址> -u -l 1400B```表示使用UDP协议并设置数据包大小为1400字节。












---