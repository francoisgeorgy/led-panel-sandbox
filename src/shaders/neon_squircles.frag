/* "Neon Squircles" by @kishimisu (2022) - https://www.shadertoy.com/view/mdjXRd
   [262 chars]

   No raymarching this time as I wanted to stay
   below 300 chars, I tried to reduce the number
   of instructions to the minimum to avoid having
   a body with brackets in the for loop.

   The layout of the code was inspired by @Xor's
   codegolfing shaders: for(..; ..; O.rgb += *magic*);
*/
void mainImage(out vec4 O, vec2 F) {
    vec2 r = iResolution.xy, u = (F+F-r)/r.y;
    O.rgb*=0.;

    for (float i; i<20.; O.rgb +=
    .004/(abs(length(u*u)-i*.04)+.005)                   // shape distance
    * (cos(i+vec3(0,1,2))+1.)                            // color
    * smoothstep(.35,.4,abs(abs(mod(iTime,2.)-i*.1)-1.)) // animation
    ) u*=mat2(cos((iTime+i++)*.03 + vec4(0,33,11,0)));   // rotation
}