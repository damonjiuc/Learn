open = ('(', '[', '{', '<')
close = (')', ']', '}', '>')
n = 19
mas = ['<f><<[u( )]x>c(g)>[z][/](( )<h{f}{h}>u)[h]{}',
'<b><h)c(y([<(x)u>t[z]])(+)>[f][(^)[-]]({f}z{t}){ }',
'{<(d)*(-<%>)>{%}(d}x)<y>({+}-))(+[[v]^])(',
'//>(x)(<)<[{z}{x(y)}a{y}( )]>{w}{h}[f][h]',
'<d>[a(f)][{z}h]([ ]<x>z)[%][g]{^([u]e)}<<d>>',
'<*[e (v){[f]t}>[]{ }[{%(%)}w](d)[(g)(e)c({g}t[w])]',
'{b}<v>[u[+]<->(g) <{f}>(g{c})[{e}h[{a[[^] {x}]{+}< >}*[x]]]',
'<e{/}>{t}(<+<[ ]a<%<g>>>{+}[v][ ]{ }<%>{w} (*)(w))(d)[z]',
'(<(g)/>[<t>z(y)<^>])<< ><(c)x><f><h>(w)<z( )>f>',
'[<[y]f[d]( )<[<t>e]^(<*>c)>><h>{w}<{[x]/[v]}(h[g])t>]{z}{{ }e}',
'<z>[{*}d(x{v})]{<w>{y}[<^>%{/}[-][e]]}<t>',
'[[w]e][%][{%}(<v>(d)<h> [<(/) >(<{/)z]{e}}[ ]^>*)]',
'[u]({<a>h[g][u]}c{g[u<^>{b}]}[%][v]( )){{[e<->[f]]-}}',
'[ <y>][<[{x} ][a]<(/( ))b>{ }{z}</>{c}/{e}>f]{[[e]<z> e]g<v>]}[u]',
'[(x{ {e[/]}})][[{g}%]^{b}(^)](v(<(-)[a]%><v[<t<y>>h]>v))',
'(z)[]{(x)c}{ }[c]{<*>f}{<a>% ((*[z])b){[ ]y}',
'{w{t}}(<<{h<+>}{*( )}[(w)[ ]z]-><[d]->(+)+<t>>)',
'{ }[[[+]w(-(<b>b(/)))]{ }{u}{[^](t]*{v}}h)[]<(z)( )(z)g>',
'(z<c(h)<[d(d)]%>>{z}{f[< >d]}[+{%}])(^)<{d}c><h><>']
def test(tested):
    brackets = []
    for i in range(len(tested)):
        if tested[i] in open:
            brackets.append(tested[i])
        elif tested[i] in close:
            if len(brackets) == 0:
                return 0
            prev = brackets.pop()
            for cur in range(len(open)):
                if prev == open[cur] and tested[i] != close[cur]:
                    return 0
    return int(len(brackets) == 0)

for i in range(n):
    print(test(mas[i]), end=' ')