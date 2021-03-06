using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004199: Nelph
/// </summary>
public class _11004199 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010646$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010647$
                // - I'm delighted to be visiting $map:02000499$ with my mother. Of course, I won't be engaging in the tourney myself. Mother and I will be quite happy to cheer the contestants on from the sidelines.
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
