using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000101: Ray
/// </summary>
public class _11000101 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000396$
    // - Yo, man! Wassup!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000398$
                // - Hey yo, do you know what hip-hop represents?
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
