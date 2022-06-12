using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000453: Brie
/// </summary>
public class _11000453 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001996$
    // - Welcome!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002000$
                // - You're not from around here, are you? 
                switch (selection) {
                    // $script:0831180407002001$
                    // - Why is the harbor so empty?
                    case 0:
                        return 41;
                    // $script:0831180407002002$
                    // - What's on the menu?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002003$
                // - Ugh, don't let me get started. Not too long ago, there was a big storm that rolled in with a tsunami, and all the regular ships we used to get here stopped coming in. Let me tell you, before the storm this place was packed with ships.
                return -1;
            case (42, 0):
                // $script:0831180407002004$
                // - If it's seafood you want, I'm your woman. Sushi plates, crab cakes, calamari, I make it all! Freshest catches you'll find anywhere without catching 'em yourself!
                return 42;
            case (42, 1):
                // $script:0831180407002005$
                // - ...And if you can wait an hour or three, I can make some for you. The storms have fouled up the fishermen, so I'm still waiting on today's catch. What a life, huh?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
