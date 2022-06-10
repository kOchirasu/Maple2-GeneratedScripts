using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001391: Yadi
/// </summary>
public class _11001391 : NpcScript {
    internal _11001391(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005391$ 
                // - $npcName:11001392[gender:1]$, are you okay?
                return true;
            case 40:
                // $script:1223165107005574$ 
                // - Our parents didn't want us, so why do <i>you</i> care?
                // $script:1223165107005575$ 
                // - They left us. Said we were cursed. I don't want to talk about it.
                // $script:1223165107005576$ 
                // - It's my job to keep $npcName:11001392[gender:1]$ safe now. She's all the family I've got.
                return true;
            case 50:
                // $script:1227015507005606$ 
                // - $npcName:11001392[gender:1]$! I'm sorry! Please... Please, say something!
                return true;
            case 60:
                // $script:0201104007005864$ 
                // - $npcName:11001392[gender:1]$, I'm so glad! Sniff...
                return true;
            default:
                return true;
        }
    }
}
