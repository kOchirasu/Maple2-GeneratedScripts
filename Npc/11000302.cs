using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000302: Udra
/// </summary>
public class _11000302 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001197$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001200$
                // - $MyPCName$, it must be an act of the divine that you and I met. My name is $npcName:11000302[gender:1]$, and I'm currently studying under $npcName:11000039[gender:1]$.
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
