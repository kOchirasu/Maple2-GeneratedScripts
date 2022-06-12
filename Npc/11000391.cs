using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000391: Rotiana
/// </summary>
public class _11000391 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001589$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001591$
                // - Have you just arrived in $map:02000001$? I came here three days ago and I'm already sick of this city. What a waste.
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
