using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003505: Rieve
/// </summary>
public class _11003505 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0816160115009002$
    // - See the hungry $itemPlural:61000002$ over there? This place is getting crowded because of them...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009003$
                // - You're way too green to cut it in Team Mushroom.
                return -1;
            case (40, 0):
                // $script:0816160115009004$
                // - Tamed monsters are called 'combat pets.' Don't forget that, 'cause it might be on the test!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
