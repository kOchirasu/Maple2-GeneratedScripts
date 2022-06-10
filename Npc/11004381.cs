using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004381: Puccini
/// </summary>
public class _11004381 : NpcScript {
    internal _11004381(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011801$ 
                // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us. 
                return true;
            case 10:
                // $script:1109213607011802$ 
                // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us. 
                return true;
            case 40:
                // $script:1120173007011874$ 
                // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us. 
                switch (selection) {
                    // $script:1120173007011875$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1120173007011876$ 
                // - I saw $npcName:11004346[gender:0]$ heading for $map:63000073$ early this morning. He goes there every day, you know. He's always got his face stuffed in a book, ignoring his adorable little sister $npcName:11004345[gender:1]$. I'd never let her get bored... So what's his problem? 
                return true;
            default:
                return true;
        }
    }
}
