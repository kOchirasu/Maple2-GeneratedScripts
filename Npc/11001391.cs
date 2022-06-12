using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001391: Yadi
/// </summary>
public class _11001391 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;60
    }

    // Select 0:
    // $script:1217193307005391$
    // - $npcName:11001392[gender:1]$, are you okay?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1223165107005574$
                // - Our parents didn't want us, so why do <i>you</i> care?
                return 40;
            case (40, 1):
                // $script:1223165107005575$
                // - They left us. Said we were cursed. I don't want to talk about it.
                return 40;
            case (40, 2):
                // $script:1223165107005576$
                // - It's my job to keep $npcName:11001392[gender:1]$ safe now. She's all the family I've got.
                return -1;
            case (50, 0):
                // $script:1227015507005606$
                // - $npcName:11001392[gender:1]$! I'm sorry! Please... Please, say something!
                return -1;
            case (60, 0):
                // $script:0201104007005864$
                // - $npcName:11001392[gender:1]$, I'm so glad! Sniff...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
