using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001389: Dalan
/// </summary>
public class _11001389 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217193307005389$
    // - Why's he so worried all the time?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1223165107005563$
                // - I have this friend named $npcName:11001396[gender:1]$. She has a house, but she practically lives out in the desert...
                return 40;
            case (40, 1):
                // $script:1223165107005564$
                // - She had a chance to get a good job in $map:02010002$, but she let it slip through her fingers. She could've been enjoying the finer things in life by now...
                return 40;
            case (40, 2):
                // $script:1223165107005565$
                // - She's always talking about ruins and secrets. Why does she let such silly nonsense weigh her down? She tried to tell me about it, but honestly, it's so boring I forgot it already...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
