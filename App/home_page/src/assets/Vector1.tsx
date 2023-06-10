export default function Vector1(props: Vector1Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 36 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 16.15 47.032 C 2.528 27.284 0 25.258 0 18 C 0 8.059 8.059 0 18 0 C 27.941 0 36 8.059 36 18 C 36 25.258 33.472 27.284 19.85 47.032 C 18.956 48.323 17.044 48.323 16.15 47.032 Z M 18 25.5 C 22.142 25.5 25.5 22.142 25.5 18 C 25.5 13.858 22.142 10.5 18 10.5 C 13.858 10.5 10.5 13.858 10.5 18 C 10.5 22.142 13.858 25.5 18 25.5 Z"
          fill="white"
         />
      </svg>
    </div>
  );
}

Vector1.defaultProps = {
  className: "",
};

interface Vector1Props {
  className: string;
}

/**
 * This component was generated from Figma with FireJet.
 * Learn more at https://www.firejet.io
 *
 * README:
 * The output code may look slightly different when copied to your codebase. To fix this:
 * 1. Include the necessary fonts. The required fonts are imported from public/index.html
 * 2. Include the global styles. They can be found in App.css
 *
 * Note: Step 2 is not required for tailwind.css output
 */
