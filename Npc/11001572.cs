using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001572: Ishura
/// </summary>
public class _11001572 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0504151707006060$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006113$
                // - The bond between our ancestors makes us strong. I couldn't be more grateful. 
                return 10;
            case (10, 1):
                // $script:0515180307006114$
                // - $MyPCName$, remember: no one crosses paths by accident. Be kind to everyone you meet, no matter how insignificant they may seem at the time.
                return -1;
            case (20, 0):
                // $script:0524142307006213$
                // - The bond between our ancestors makes us strong. I couldn't be more grateful. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
