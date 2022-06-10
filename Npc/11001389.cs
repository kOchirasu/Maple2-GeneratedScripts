using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001389: Dalan
/// </summary>
public class _11001389 : NpcScript {
    internal _11001389(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005389$ 
                // - Why's he so worried all the time? 
                return true;
            case 40:
                // $script:1223165107005563$ 
                // - I have this friend named $npcName:11001396[gender:1]$. She has a house, but she practically lives out in the desert... 
                // $script:1223165107005564$ 
                // - She had a chance to get a good job in $map:02010002$, but she let it slip through her fingers. She could've been enjoying the finer things in life by now... 
                // $script:1223165107005565$ 
                // - She's always talking about ruins and secrets. Why does she let such silly nonsense weigh her down? She tried to tell me about it, but honestly, it's so boring I forgot it already... 
                return true;
            default:
                return true;
        }
    }
}
