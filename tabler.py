"""
tabler.py
Creates tables in HTML for Salstat
Submit a list of [heading: value] pairs in the desired order
p-values are automatically formatted as %1.6f (all other floats as %5.3f?)
"""

def table(ListofLists):
    ln1 = '<table class="table table-striped"><tr>'
    ln2 = '<tr>'
    for List in ListofLists:
        key = List[0]
        val = List[1]
        headhtml = '<th>%s</th>'%key
        if key == 'p':
            try:
                foothtml = '<td>%1.6f</td>'%val
            except TypeError:
                foothtml = '<td>n/a</td>'
        elif type(val) is int:
            foothtml = '<td>%d</td>'%val
        elif (type(val) is str) or (type(val) is unicode):
            foothtml = '<td>%s</td>'%val
        elif type(val) is float:
            fltstr = str(val)
            foothtml = '<td>%s</td>'%fltstr
            # really need to figure out what parameters make a good display for each number
        ln1 = ln1 + headhtml
        ln2 = ln2 + foothtml
    ln1 = ln1 + '</tr>' + ln2 + '</tr>\n</table>\n'
    return ln1

def vtable(List):
    key = List[0]
    vals = List[1:]
    btn_id = ' id="%s"'%key
    chartbutton = '<a class="btn btn-mini dropdown-toggle"%s data-toggle="dropdown" \
            href="#">Chart</a>\n'%btn_id
    linehtml = '<tr><td>%s %s</td>'%(chartbutton, key)
    for val in vals:
        if key == 'p':
            try:
                linehtml = '<td>%1.6f</td>'%val
            except TypeError:
                linehtml = '<td>n/a</td>'
        elif type(val) is int:
            linehtml = linehtml + '<td>%d</td>'%val
        elif (type(val) is str) or (type(val) is unicode):
            linehtml = linehtml + '<td>%s</td>'%val
        elif type(val) is float:
            linehtml = linehtml + '<td>%s</td>'%str(val)
    linehtml = linehtml + '</tr>\n'
    return linehtml

if __name__ == '__main__':
    a1 = ['Variable 1','Var001']
    a2 = ['Variable 2','Var002']
    a3 = ['df',99]
    a4 = ['t',30.0001]
    a5 = ['p',0.003]
    a = [a1,a2,a3,a4,a5]
    print table(a)

