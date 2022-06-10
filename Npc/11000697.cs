using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000697: Blind Rio
/// </summary>
public class _11000697 : NpcScript {
    internal _11000697(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002813$ 
                // - ... 
                return true;
            case 50:
                // $script:0831180407002816$ 
                // - Mm... Who's there? I can't see you, but I can sense your burning soul. 
                switch (selection) {
                    // $script:0831180407002817$
                    // - What happened?
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407002818$
                    // - What's the $map:65000002$?
                    case 1:
                        Id = 52;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407002819$ 
                // - ...Do you mean my eyes? As you can see, I'm blind. I committed a sin so grave that I gave up my eyes in penance. 
                // $script:0831180407002820$ 
                // - I can tell you want to hear my story. I assume $npcName:11000289[gender:0]$ told you about the arena. That is where you can always find a fair fight. No battles to the death, just competitions of strength. 
                // $script:0831180407002821$ 
                // - But I killed someone there. It was an accident, and everyone who watched our fight agreed that it was unavoidable, but I couldn't forgive myself. 
                // $script:0831180407002822$ 
                // - That's why I decided to hide in the darkness. That's all. 
                return true;
            case 52:
                // $script:0831180407002823$ 
                // - You must be interested in the $map:65000002$. But as its name suggests, it's a dangerous place. Everyone in there is determined to hurt each other in a contest of strength. If you want to join in, you'd better prepare well. 
                // $script:0831180407002824$ 
                // - The $map:65000002$ is a battleground in which up to 10 warriors battle each other for points, and whoever beats more competitors than the others wins. When you beat another warrior, you get points. When you are beaten, you lose them. 
                // $script:0831180407002825$ 
                // - Since so many warriors fight each other at the same time, sometimes things get really chaotic. The winner might not be the strongest of them all, but the smartest. 
                // $script:0831180407002826$ 
                // - It's always good to test your strength, but be careful not to let your excitement get the best of you. That's all I have to tell you. Be on your way. 
                return true;
            default:
                return true;
        }
    }
}
