using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000359: Hendel
/// </summary>
public class _11000359 : NpcScript {
    internal _11000359(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001489$ 
                // - May I help you?
                return true;
            case 20:
                // $script:0831180407001491$ 
                // - Are you traveling? You look like you're about my son's age.
                // $script:0831180407001492$ 
                // - $npcName:11000360[gender:0]$ is my only child. He left home recently, wanting to strike out on his own. If only he knew how much that hurt his mother.
                // $script:0831180407001493$ 
                // - The day before yesterday I got a letter from $npcName:11000360[gender:0]$. He must've written it somewhere around here... even the edges are singed. So I bought an ice pack to keep him cool.
                // $script:0831180407001494$ 
                // - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
                return true;
            case 30:
                // $script:0831180407001495$ 
                // - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
                return true;
            default:
                return true;
        }
    }
}
