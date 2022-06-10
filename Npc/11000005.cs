using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000005: Anne
/// </summary>
public class _11000005 : NpcScript {
    internal _11000005(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 80;90
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000020$ 
                // - Let's see... So, this book goes... 
                return true;
            case 80:
                // $script:0116174407009791$ 
                // - Is there anything that you can't learn in a book?
                // $script:0116174407009792$ 
                // - Here's a familiar face. Have you finally decided to focus on higher education? I knew you'd come around eventually.
                switch (selection) {
                    // $script:0116174407009793$
                    // - Actually, I'm here to do some research on Orbis.
                    case 0:
                        Id = 81;
                        return false;
                }
                return true;
            case 81:
                // $script:0116174407009794$ 
                // - Ah, the floating city. It was world-famous for its astonishing vistas. Unfortunately, it was destroyed in the war.
                // $script:0116174407009795$ 
                // - Even though the city is in ruins, the city center still burns to this day. Not a very pleasant place to live these days.
                switch (selection) {
                    // $script:0116174407009796$
                    // - What else can you tell me about it?
                    case 0:
                        Id = 82;
                        return false;
                }
                return true;
            case 82:
                // $script:0116174407009797$ 
                // - That depends. What, specifically, do you want to know?
                switch (selection) {
                    // $script:0116174407009798$
                    // - If Orbis is still on fire, where is the heat coming from?
                    case 0:
                        Id = 83;
                        return false;
                }
                return true;
            case 83:
                // $script:0116174407009799$ 
                // - Ah, now that is a curious question! I think I read something about that once...
                // $script:0116174407009800$ 
                // - In Orbis, the floating city, a very special cave exists. A cave where magma flows endlessly.
                switch (selection) {
                    // $script:0116174407009801$
                    // - Do you know where the cave is?
                    case 0:
                        Id = 84;
                        return false;
                }
                return true;
            case 84:
                // $script:0116174407009802$ 
                // - No, but it shouldn't be too hard for me to find out. Actually getting to Orbis, however, is a fool's errand. I doubt anybody could survive there for long.
                switch (selection) {
                    // $script:0116174407009803$
                    // - It's a good thing I'm not just anybody.
                    case 0:
                        Id = 85;
                        return false;
                }
                return true;
            case 85:
                // $script:0116174407009804$ 
                // - Hopelessly reckless, as usual. I'll tell you where to go, but that's it. I'll have nothing more to do with this.
                switch (selection) {
                    // $script:0116174407009805$
                    // - Thank you for your time.
                    case 0:
                        Id = 86;
                        return false;
                }
                return true;
            case 86:
                // $script:0116174407009806$ 
                // - Don't mention it. Please. You'll forgive me for not seeing you off...
                return true;
            case 90:
                // $script:0504174607009860$ 
                // - Is there nothing you can't learn from a book?
                return true;
            default:
                return true;
        }
    }
}
