//https://iquilezles.org/articles/palettes/
vec3 palette( float t ) {
    vec3 a = vec3(0.5, 0.5, 0.5);
    vec3 b = vec3(0.5, 0.5, 0.5);
    vec3 c = vec3(1.0, 1.0, 1.0);
    vec3 d = vec3(0.263,0.416,0.557);
    return a + b*cos( 6.28318*(c*t+d) );
}








void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    fragColor = vec4(uv.x, 0.0, 0.0, 1.0);
}




/**

vec2 uv = fragCoord / iResolution.xy;
fragColor = vec4(uv.x, 0.0, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy;
fragColor = vec4(uv.x, uv.y, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy;
uv = uv - 0.5;
fragColor = vec4(uv.x, uv.y, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy;
uv = (uv - 0.5) * 2.0;
fragColor = vec4(uv.x, uv.y, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy * 2.0 - 1.0;
fragColor = vec4(uv.x, uv.y, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy * 2.0 - 1.0;
float d = length(uv)
fragColor = vec4(d, 0.0, 0.0, 1.0);

vec2 uv = fragCoord / iResolution.xy * 2.0 - 1.0;
uv.x *= iResolution.x / iResolution.y;
float d = length(uv)
fragColor = vec4(d, 0.0, 0.0, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
fragColor = vec4(d, 0.0, 0.0, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d -= 0.5;
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d -= 0.5;
d = abs(d);
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d -= 0.5;
d = abs(d);
d = step(0.1, d);
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d -= 0.5;
d = abs(d);
d = smoothstep(0.0, 0.1, d);
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d = sin(d * 8.0) / 8.0;
d = abs(d);
d = smoothstep(0.0, 0.1, d);
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = smoothstep(0.0, 0.1, d);
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
fragColor = vec4(d, d, d, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
vec3 col = vec3(1.0, 0.0, 0.0);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
float d = length(uv);
vec3 col = palette(d + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
uv = fract(uv);
float d = length(uv);
vec3 col = palette(d + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
uv *= 2.0;
uv = fract(uv);
float d = length(uv);
vec3 col = palette(d + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
uv = fract(uv * 2.0) - 0.5;
float d = length(uv);
vec3 col = palette(d + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
vec2 uv0 = uv;
uv = fract(uv * 2.0) - 0.5;
float d = length(uv);
vec3 col = palette(length(uv0) + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
col *= d;
fragColor = vec4(col, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
vec2 uv0 = uv;
vec3 finalColor = vec3(0.0);
uv = fract(uv * 2.0) - 0.5;
float d = length(uv);
vec3 col = palette(length(uv0) + iTime);
d = sin(d * 8.0 + iTime) / 8.0;
d = abs(d);
d = 0.02 / d;
finalColor += col * d;
fragColor = vec4(finalColor, 1.0);

vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
vec2 uv0 = uv;
vec3 finalColor = vec3(0.0);
for (float i = 0.0; i < 4.0; i++) {
    uv = fract(uv * 1.5) - 0.5;
    float d = length(uv) * exp(-length(uv0));
    vec3 col = palette(length(uv0) + i*.4 + iTime*.4);
    d = sin(d*8. + iTime)/8.;
    d = abs(d);
    d = pow(0.01 / d, 1.2);
    finalColor += col * d;
}
fragColor = vec4(finalColor, 1.0);

//https://www.shadertoy.com/view/mtyGWy
void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    vec2 uv0 = uv;
    vec3 finalColor = vec3(0.0);

    for (float i = 0.0; i < 4.0; i++) {
        uv = fract(uv * 1.5) - 0.5;

        float d = length(uv) * exp(-length(uv0));

        vec3 col = palette(length(uv0) + i*.4 + iTime*.4);

        d = sin(d*8. + iTime)/8.;
        d = abs(d);

        d = pow(0.01 / d, 1.2);

        finalColor += col * d;
    }

    fragColor = vec4(finalColor, 1.0);
}
*/