def calc(str):
	import re
	token=[float(y) if y[0] in '0123456789' else y for y in [x[0] for x in re.findall('(\d+(\.\d+)?([eE][-+]?\d+)?|[-+*/()])',str)]]
	opert,right={'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y},{'(':0,'+':1,'-':1,'*':2,'/':2,')':3}
	ans,stk=[],['(',]
	def clear(a,b,c):
		while c(b):
			x=a.pop()
			a[-1]=opert[b.pop()](ans[-1],x)
	try:
		for ele in token:
			if ele in right:
				{'(':lambda :stk.append(ele),
				 ')':lambda :clear(ans,stk,lambda a:a[-1]!='(') or stk.pop(),
				}.get(ele,lambda : clear(ans,stk,lambda a:right[a[-1]]>=right[ele]) or stk.append(ele))()
			else:
				ans.append(ele)
		clear(ans,stk,lambda a:a[-1]!='(')
		return ans[0]
	except:
		return None
	
if __name__=='__main__':
	while True:
		ans=calc(raw_input('> '))
		if ans:print ' ',ans
