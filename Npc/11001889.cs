using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001889: Oska
/// </summary>
public class _11001889 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1027193507007342$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1027193507007343$
                // - Thanks for all the hard work, $MyPCName$. 
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
