
from fpdf import FPDF


def parenting(array):
    relatives = {}
    for item in array:
        if item['parentId'] in relatives:
            match = relatives[item['parentId']]
            if match.get('children') is None:
                match['children'] = []
            match['children'].append(item)
        relatives[item['id']] = item
    return [item for item in relatives.values() if item.get('children')]


def report(array):
    pdf = FPDF()
    pdf.set_font('Arial', '', 14)
    pdf.add_page()
    for item in parenting(array):
        id, parentid, children = (
            item['id'],
            item['parentId'],
            item['children']
        )
        text = f'id:{id} parentId:{parentid} children:{children}'
        pdf.cell(0, 10, txt=text, ln=1)
    pdf.output('report.pdf')


if __name__ == '__main__':
    array = [
        {'id': 1, 'parentId': 0},
        {'id': 2, 'parentId': 0},
        {'id': 3, 'parentId': 1},
        {'id': 4, 'parentId': 1},
        {'id': 5, 'parentId': 2},
        {'id': 6, 'parentId': 4},
        {'id': 7, 'parentId': 5},
    ]
    print(report(array))
