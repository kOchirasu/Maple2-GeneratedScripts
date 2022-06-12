using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004197: Asimov
/// </summary>
public class _11004197 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010642$
    // - Do you need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010643$
                // - I'm wise enough to admit I've gotten too old to keep up with the youth of today. When you reach a certain age, you've just got to step out of the way and leave things to the next generation.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
