<%inherit file="base.mako"/>
<h2> Coordinates table </h2>
<table>
<tr>
<th width="60">&nbsp;PATH ID</th>
<th width="100">POINT NUM </th>
<th width="200">LATITUDE</th>
<th width="200">LONGITUDE</th>
</tr>
</table>







%for category in acc2:
<table>
<tr>
<td width="60">
<h3>&nbsp;&nbsp;&nbsp;${category.path_id}</h3>
</td>

<td width="100">
<h3>&nbsp;&nbsp;&nbsp;${category.Point}</h3>
</td>


<td width="200">
<h3>&nbsp;&nbsp;${category.latitude}</h3>
</td>
<td width="200">
<h3>&nbsp;&nbsp;${category.longitude}</h3>
</td>
</tr>
</table>


%endfor
