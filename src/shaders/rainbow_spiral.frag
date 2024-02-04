/* "Rainbow Spiral" by @kishimisu (2022) - https://www.shadertoy.com/view/clfGW8
   [226 chars] */

void mainImage(out vec4 O, vec2 F) {
    vec2 r = iResolution.xy;
    float i = .3, l = length(F+=F-r)/r.y + i, t = iTime;

    for (O *= 0.; i < 12.;
         O += length(min(r.y/abs(F),r))/3e2*(cos(++t+i+vec4(0,1,2,0))*l+l))
         F *= mat2(cos(l*.2-i++*--t/1e2+vec4(0,33,11,0)));
}