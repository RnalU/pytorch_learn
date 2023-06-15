from visualdl import LogWriter
from visualdl.server import app

"""
--logdir	设定日志所在目录，可以指定多个目录，VisualDL将遍历并且迭代寻找指定目录的子目录，将所有实验结果进行可视化
--model	设定模型文件路径(非文件夹路径)，VisualDL将在此路径指定的模型文件进行可视化，目前可支持PaddlePaddle、ONNX、Keras、Core ML、Caffe等多种模型结构，详情可查看graph支持模型种类
--host	设定IP，默认为127.0.0.1
--port	设定端口，默认为8040
--cache-timeout	后端缓存时间，在缓存时间内前端多次请求同一url，返回的数据从缓存中获取，默认为20秒
--language	VisualDL面板语言，可指定为'EN'或'ZH'，默认为浏览器使用语言
--public-path	VisualDL面板URL路径，默认是'/app'，即访问地址为'http://<host>:<port>/app'
--api-only	是否只提供API，如果设置此参数，则VisualDL不提供页面展示，只提供API服务，此时API地址为'http://<host>:<port>/<public_path>/api'；
若没有设置public_path参数，则默认为'http://<host>:<port>/api'
"""


# 此demo演示了两次实验的超参数记录，以第一次实验数据为例，首先在`add_hparams`接口中记录
# 超参数`hparams`的数据，再标定了稍后要记录的`metrics`名称，最后通过`add_scalar`再具体
# 记录`metrics`的数据。此处需注意`add_hparams`接口中的`metrics_list`参数需要包含`add_scalar`
# 接口的`tag`参数。
if __name__ == '__main__':
    # with LogWriter(logdir="./log_dir/scalar/train") as writer:
    #     # 使用scalar组件记录一个标量数据
    #     writer.add_scalar(tag="acc", step=1, value=0.5678)
    #     writer.add_scalar(tag="acc", step=2, value=0.6878)
    #     writer.add_scalar(tag="acc", step=3, value=0.9878)
    #
    # # 记录第一次实验数据
    # with LogWriter('./log_dir/hparams_test/train/run1') as writer:
    #     # 记录hparams数值和metrics名称
    #     writer.add_hparams(hparams_dict={'lr': 0.1, 'bsize': 1, 'opt': 'sgd'},
    #                        metrics_list=['hparam/accuracy', 'hparam/loss'])
    #     # 通过将add_scalar接口中的tag与metrics名称对应，记录一次实验中不同step的metrics数值
    #     for i in range(10):
    #         writer.add_scalar(tag='hparam/accuracy', value=i, step=i)
    #         writer.add_scalar(tag='hparam/loss', value=2*i, step=i)
    #
    # # 记录第二次实验数据
    # with LogWriter('./log_dir/hparams_test/train/run2') as writer:
    #     # 记录hparams数值和metrics名称
    #     writer.add_hparams(hparams_dict={'lr': 0.2, 'bsize': 2, 'opt': 'relu'},
    #                        metrics_list=['hparam/accuracy', 'hparam/loss'])
    #     # 通过将add_scalar接口中的tag与metrics名称对应，记录一次实验中不同step的metrics数值
    #     for i in range(10):
    #         writer.add_scalar(tag='hparam/accuracy', value=1.0/(i+1), step=i)
    #         writer.add_scalar(tag='hparam/loss', value=5*i, step=i)

    app.run("log_dir",
            host="127.0.0.1",
            port=8080,
            cache_timeout=20,
            language=None,
            public_path=None,
            api_only=False,
            open_browser=True
            )
