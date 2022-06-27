res=[[0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0]]
for i in range(6):
    b = input().split(", ")
    for j in range(6):
        res[i][j] = int(b[j])

ans = f"""
<p>Между населёнными пунктами A, B, C, D, E, F построены дороги, протяжённость которых приведена в таблице. Отсутствие числа в таблице значает, что прямой дороги между пунктами нет.</p>

<table align="center" border="1" cellpadding="5" cellspacing="0" style="height:100px; width:500px">
	<tbody>
		<tr>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">A</td>
			<td style="height:25px; width:50px text-align:center">B</td>
			<td style="height:25px; width:50px text-align:center">C</td>
			<td style="height:25px; width:50px text-align:center">D</td>
			<td style="height:25px; width:50px text-align:center">E</td>
			<td style="height:25px; width:50px align:center">F</td>
		</tr>
		<tr>
			<td dir="rtl" style="height:25px; width:50px text-align:center">A</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">{res[0][1]}</td>
			<td style="height:25px; width:50px text-align:center">{res[0][2]}</td>
			<td style="height:25px; width:50px text-align:center">{res[0][3]}</td>
			<td style="height:25px; width:50px text-align:center">{res[0][4]}</td>
			<td style="height:25px; width:50px text-align:center">{res[0][5]}</td>
		</tr>
		<tr>
			<td style="height:25px; width:50px text-align:center">B</td>
			<td dir="rtl" style="height:25px; width:50px text-align:center">{res[1][0]}</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">{res[1][2]}</td>
			<td style="height:25px; width:50px text-align:center">{res[1][3]}</td>
			<td style="height:25px; width:50px text-align:center">{res[1][4]}</td>
			<td style="height:25px; width:50px text-align:center">{res[1][5]}</td>
		</tr>
		<tr>
			<td style="height:25px; width:50px text-align:center">C</td>
			<td style="height:25px; width:50px text-align:center">{res[2][0]}</td>
			<td style="height:25px; width:50px text-align:center">{res[2][1]}</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">{res[2][3]}</td>
			<td style="height:25px; width:50px text-align:center">{res[2][4]}</td>
			<td style="height:25px; width:50px text-align:center">{res[2][5]}</td>
		</tr>
		<tr>
			<td style="height:25px; width:50px text-align:center">&nbsp;D</td>
			<td style="height:25px; width:50px text-align:center">{res[3][0]}</td>
			<td style="height:25px; width:50px text-align:center">{res[3][1]}</td>
			<td style="height:25px; width:50px text-align:center">{res[3][2]}</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">{res[3][4]}</td>
			<td style="height:25px; width:50px text-align:center">{res[3][5]}</td>
		</tr>
		<tr>
			<td style="height:25px; width:50px text-align:center">E</td>
			<td style="height:25px; width:50px text-align:center">{res[4][0]}</td>
			<td style="height:25px; width:50px text-align:center">{res[4][1]}</td>
			<td style="height:25px; width:50px text-align:center">{res[4][2]}</td>
			<td style="height:25px; width:50px text-align:center">{res[4][3]}</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
			<td style="height:25px; width:50px text-align:center">{res[4][5]}</td>
		</tr>
		<tr>
			<td style="height:25px; width:50px text-align:center">F</td>
			<td style="height:25px; width:50px text-align:center">{res[5][0]}</td>
			<td style="height:25px; width:50px text-align:center">{res[5][1]}</td>
			<td style="height:25px; width:50px text-align:center">{res[5][2]}</td>
			<td style="height:25px; width:50px text-align:center">{res[5][3]}</td>
			<td style="height:25px; width:50px text-align:center">{res[5][4]}</td>
			<td style="height:25px; width:50px background-color:#66ffff; text-align:center">&nbsp;</td>
		</tr>
	</tbody>
</table>
<p>Определите длину кратчайшего пути между пунктами A и F (при условии, что передвигаться можно только по построенным дорогам).</p>
<p style="text-align:center">&nbsp;</p>
"""
print(ans)