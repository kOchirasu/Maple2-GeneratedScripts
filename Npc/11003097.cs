using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003097: SwagWagon Guild Leader
/// </summary>
public class _11003097 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0119135307007815$
    // - Yo, what's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0119135307007818$
                // - Yo, you looking for a guild? This is the Swag Wagon, a crew of hip-hop dancers.
                switch (selection) {
                    // $script:0119135307007819$
                    // - I totally want to join your guild!
                    case 0:
                        return 31;
                    // $script:0119135307007820$
                    // - Not really my scene, but thanks.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0119135307007821$
                // - I bet you do, but we're full up. You might be able to find another crew, or start your own. Don't expect to compete with us though, heh. 
                return -1;
            case (32, 0):
                // $script:0119135307007822$
                // - I wasn't... Uhh, okay, whatever. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
