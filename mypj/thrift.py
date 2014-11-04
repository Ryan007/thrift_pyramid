from pyramid.view import view_config
from pyramid.response import Response

import thriftpy
calc_thrift = thriftpy.load("mypj/thrift/cal.thrift", module_name="calc_thrift")

from thriftpy.protocol import TCyBinaryProtocolFactory
from thriftpy.transport import TCyBufferedTransportFactory
from thriftpy.rpc import client_context



@view_config(route_name='thrift', renderer='string')
def thrift(request):
	with client_context(calc_thrift.Calculator, '127.0.0.1', 6000,
                        proto_factory=TCyBinaryProtocolFactory(),
                        trans_factory=TCyBufferedTransportFactory()) as cal:
		a = cal.mult(5, 2)
		b = cal.sub(7, 3)
		c = cal.sub(6, 4)
		d = cal.mult(b, 10)
		e = cal.add(a, d)
		f = cal.div(e, c)
		
		return Response(str(b))
