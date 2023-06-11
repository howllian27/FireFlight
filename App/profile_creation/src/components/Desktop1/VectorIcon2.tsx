import { Link } from 'react-router-dom';
import { memo, SVGProps } from 'react';

const VectorIcon2 = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 19 30' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path
      d='M18.3528 16.5933L5.84474 29.3393C4.98021 30.2202 3.58226 30.2202 2.72693 29.3393L0.648393 27.2212C-0.216131 26.3402 -0.216131 24.9157 0.648393 24.044L9.51437 15.0094L0.648393 5.9747C-0.216131 5.09372 -0.216131 3.66917 0.648393 2.79756L2.71773 0.660731C3.58226 -0.220244 4.98021 -0.220244 5.83554 0.660731L18.3436 13.4067C19.2173 14.2877 19.2173 15.7123 18.3528 16.5933V16.5933Z'
      fill='#FC5710'
    />
  </svg>
);
const Memo = memo(VectorIcon2);
export { Memo as VectorIcon2 };
