using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003556: Dr. Galileo's Hologram
/// </summary>
public class _11003556 : NpcScript {
    protected override int First() {
        return 30;
    }

    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0907171907008963$
                // - Hello in there. The simulation is stable, and it appears the test is proceeding nicely. You look a bit singed around the edges, but otherwise in good spirits.
                switch (selection) {
                    // $script:0907171907008964$
                    // - What are you doing here?
                    case 0:
                        return 31;
                    // $script:0907171907008965$
                    // - What now?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0907171907008966$
                // - I came to check on your progress. What do you think of my hologram? With my current avatar settings, I can observe the test without interfering.
                return 31;
            case (31, 1):
                // $script:0907171907008967$
                // - Interfering with the results of my own test would invalidate all of the data I've collected, after all. Which would be quite silly after all the trouble I went through selecting test subjects.
                return 31;
            case (31, 2):
                // $script:0907171907008968$
                // - Don't mind me. I'll be here observing. Just go about your business as if I weren't even here.
                switch (selection) {
                    // $script:0907171907008969$
                    // - What now?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0907171907008970$
                // - Erm... You don't know? 
                return 32;
            case (32, 1):
                // $script:0907173207008999$
                // - <font color="#909090" size="20">Should I tell them? I suppose they'll figure it out sooner or later... I'll just consider this a minor acceleration in the test plan.</font>
                switch (selection) {
                    // $script:0907173207009000$
                    // - So... What am I supposed to do again?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0907171907008972$
                // - Well, I suspect I've already told you that if you hit a roadblock in the simulation, you'll need a special override code to proceed. Do you have <font color="#ffd200">$item:20000627$</font> in your possession?
                switch (selection) {
                    // $script:0907171907008973$
                    // - I've got it right here.
                    case 0:
                        return 35;
                    // $script:0907171907008974$
                    // - Nope.
                    case 1:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0907171907008975$
                // - Well now... That's a bit disappointing. I'm afraid if you want to climb any higher, you'll need <font color="#ffd200">$item:20000627$</font>.
                //   You can purchase it from your Guild Supply Merchant. 
                return 34;
            case (34, 1):
                // $script:0907171907008976$
                // - It's a bit unfortunate, but unless one of your party members has the code in their possession, it might be prudent to restart this test at a later date.
                return -1;
            case (35, 0):
                // $script:0907171907008977$
                // - Ah, excellent. Well now is the time to put it to work. Using the <font color="#ffd200">$item:20000627$</font> should alter your avatar's biometric data, transforming you—as you might have guessed—into a $npc:34000100$, which will allow you to safely reach the summit.
                return 35;
            case (35, 1):
                // $script:0907171907008978$
                // - Once you've transformed into a $npc:34000100$, you'll be virtually impervious to the heat of the lava. However, $npc:34000100$ aren't very strong flyers, so your best recourse will be climbing from ledge to ledge. Oh! And tapping the <font color="#ffd200">X key</font> will give you a nice boost of speed.
                return 35;
            case (35, 2):
                // $script:0907171907008979$
                // - $npcPlural:34000100$ are not overly protective of their young, so you should have no difficulty collecting their eggs. However, they are particularly ornery and aggressive in general, so I wouldn't recommend getting too close to the adults.
                return 35;
            case (35, 3):
                // $script:0907171907008980$
                // - See that glowing circle around them? It represents their natural threat response. Step foot inside, and you'll be met with their terrible fire breath, which burns far hotter than the lava pools they call home.
                return 35;
            case (35, 4):
                // $script:0907171907008981$
                // - The volcano's summit is their breeding ground. Your task is to reach it, and collect five eggs. Good luck up there!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Next,
            (35, 1) => NpcTalkButton.Next,
            (35, 2) => NpcTalkButton.Next,
            (35, 3) => NpcTalkButton.Next,
            (35, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
