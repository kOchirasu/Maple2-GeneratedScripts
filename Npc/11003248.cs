using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003248: Strange Wall
/// </summary>
public class _11003248 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008163$
    // - <font color="#909090">(You feel a chill from behind the waterfall.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008164$
                // - <font color="#909090">(Maybe there's something there... or maybe not.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
