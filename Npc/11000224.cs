using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000224: Linda
/// </summary>
public class _11000224 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000976$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000978$
                // - My boyfriend and I came here for a picnic, and we ended up fighting because he kept looking at other girls. The nerve!
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
