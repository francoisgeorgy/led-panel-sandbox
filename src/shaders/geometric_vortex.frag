#define PI       3.141592
#define S(a,b,d) mix(a, b, sin(d + n*PI*2.)*.5+.5)
#define rot(a)   mat2(cos( a +vec4(0,33,11,0)))
#define n        (-iTime*.04+.03)

void mainImage(out vec4 O, in vec2 F) {
    vec2 u = (F - iResolution.xy*.5)/iResolution.y;
    for (float s = 0.; s < 3.; s++) { float p = 9.;
    for (float i = 0.; i < 25.; i++) {
        vec2  a = fract(rot(i*sin(n*PI*2.)*.25)*u*(i+S(1., 4., PI/2.))+.5)-.5;
        float r = mix(length(a), abs(a.x) + abs(a.y), S(0., 1.,));
        float t = abs(r + .1 - s*.02 - i*S(0.005, 0.05,));
        p = min(p, smoothstep(0., .1 + s*i*S(.0, .015, PI), t*S(s*.1 + .14, .2,)) +
            smoothstep(0., 20., i*S(.45, 1.,)) + smoothstep(0., 1., length(u)*i*.08));
    } O[int(s)] = .1/p;
    } O.a=1.;
}

// 454 chars by @FabriceNeyret2

// #define S(d) (sin((d+n)*6.28)*.5+.5)
// #define B smoothstep(0.,
// void mainImage(out vec4 O, vec2 F) {
//     vec2 a=iResolution.xy,u=(F-a*.5)/a.y;
//     for(float n=.03-iTime*.04,p,i,t,s=0.;s<3.;O[int(s)]=.1/p,s++)
//     for(p=9.,i=0.;i<25.;i++)a=abs(fract(mat2(cos(
//     i*(S()-.5)/2.+vec4(0,33,11,0)))*u*(i+1.+3.*S(.25))+.5)-.5),
//     p=min(p,B.1+s*i*.015*S(.5),abs(mix(length(a),a.x+a.y,S())
//     +.1-s*.02-i*.045*(.11+ S()))*(s*.1+.14+.1*(.6-s)*S()))
//     +B 20.,i*(.45+.55*S()))+B 1.,length(u)*i*.08));
// }