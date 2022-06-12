using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003266: Eks
/// </summary>
public class _11003266 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008212$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008213$
                // - My head is throbbing. Shoulder, knees, and toes, too. Mark my words, there's a storm brewing. 
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
