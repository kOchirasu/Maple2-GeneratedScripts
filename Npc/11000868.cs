using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000868: Tess
/// </summary>
public class _11000868 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003139$
    // - Oh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003141$
                // - Are they doing this to me because I'm an intern? I didn't become a researcher to run errands!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
