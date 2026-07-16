import numpy as np

from app.ai.ml.future_pipeline.temporal_buffer import (
    TemporalBuffer
)

from app.ai.ml.future_pipeline.sequence_generator import (
    SequenceGenerator
)

from app.ai.ml.future_pipeline.sentence_builder import (
    SentenceBuilder
)


def main():

    print("\n========== Future Pipeline Test ==========\n")

    # ---------------------------------------------------------
    # Create Temporal Buffer
    # ---------------------------------------------------------

    buffer = TemporalBuffer(max_frames=20)

    # Simulate 20 frames
    for i in range(20):

        landmarks = np.random.rand(63)

        buffer.add_frame(landmarks)

    print("Frames Stored :", len(buffer.get_sequence()))
    print("Buffer Ready  :", buffer.is_ready())

    # ---------------------------------------------------------
    # Generate Sequence
    # ---------------------------------------------------------

    generator = SequenceGenerator()

    sequence = generator.generate(
        buffer.get_sequence()
    )

    print()
    print("Sequence Shape  :", generator.sequence_shape(sequence))
    print("Sequence Length :", generator.sequence_length(sequence))

    # ---------------------------------------------------------
    # Test Sentence Builder
    # ---------------------------------------------------------

    builder = SentenceBuilder()

    builder.add_prediction("HELLO")
    builder.add_prediction("HOW")
    builder.add_prediction("ARE")
    builder.add_prediction("YOU")

    print()
    print("Sentence :")
    print(builder.get_sentence())


if __name__ == "__main__":
    main()