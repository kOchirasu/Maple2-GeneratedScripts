using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003889: Piris
/// </summary>
public class _11003889 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009933$
    // - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009934$
                // - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
                return -1;
            case (30, 0):
                // $script:0515102507009935$
                // - I'll punish any who threaten the seas. Even you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
