using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003891: Dark Lord
/// </summary>
public class _11003891 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009939$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009940$
                // - What is it?
                return -1;
            case (30, 0):
                // $script:0515102507009941$
                // - Even though the request came from the $npc:11003894[gender:0]$, I'm not interested.
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
