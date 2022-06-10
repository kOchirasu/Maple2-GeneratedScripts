using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000453: Brie
/// </summary>
public class _11000453 : NpcScript {
    internal _11000453(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001996$ 
                // - Welcome!
                return true;
            case 40:
                // $script:0831180407002000$ 
                // - You're not from around here, are you? 
                switch (selection) {
                    // $script:0831180407002001$
                    // - Why is the harbor so empty?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002002$
                    // - What's on the menu?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002003$ 
                // - Ugh, don't let me get started. Not too long ago, there was a big storm that rolled in with a tsunami, and all the regular ships we used to get here stopped coming in. Let me tell you, before the storm this place was packed with ships.
                return true;
            case 42:
                // $script:0831180407002004$ 
                // - If it's seafood you want, I'm your woman. Sushi plates, crab cakes, calamari, I make it all! Freshest catches you'll find anywhere without catching 'em yourself!
                // $script:0831180407002005$ 
                // - ...And if you can wait an hour or three, I can make some for you. The storms have fouled up the fishermen, so I'm still waiting on today's catch. What a life, huh?
                return true;
            default:
                return true;
        }
    }
}
