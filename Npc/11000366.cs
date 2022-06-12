using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000366: Janine
/// </summary>
public class _11000366 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001511$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001513$
                // - Do you know what makes cats so appealing? It's how independent they are! Though... it's possible for them to be too independent. Like $npcName:11000367$, for example.
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
