using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004331: Orde
/// </summary>
public class _11004331 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011633$
        // - Those four... It can't be...
        // Select 20:
        // $script:1010140307011551$
        // - Those four... It can't be...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011634$
                // - Children of the dragon... here? Am I dreaming?
                return -1;
            case (30, 0):
                // $script:1010140307011552$
                // - Children of the dragon... here? Am I dreaming?
                switch (selection) {
                    // $script:1010140307011553$
                    // - (Tap her gently on the shoulder.)
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011554$
                // - Ahh! Don't sneak up on a girl like that!
                return 40;
            case (40, 1):
                // $script:1010140307011555$
                // - Oh, it's you. I didn't expect to run into you here.
                return 40;
            case (40, 2):
                // $script:1010140307011556$
                // - I'm busy right now. Can we talk later?
                switch (selection) {
                    // $script:1010140307011557$
                    // - What are you doing?
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011558$
                // - It's top-secret!
                return 50;
            case (50, 1):
                // $script:1010140307011559$
                // - Actually, you'll never believe it. Those kids raised by the last dragon master? They're <b>here</b>!
                return 50;
            case (50, 2):
                // $script:1010140307011560$
                // - I heard the rumors. That's the only reason I was willing to come schlep all the way here with $npcName:11004332[gender:1]$. But it turns out they were true!
                return 50;
            case (50, 3):
                // $script:1010140307011561$
                // - See that girl with the blonde hair, way over there? I can smell her dragon juju from here. Unless I'm imagining things...
                return 50;
            case (50, 4):
                // $script:1010140307011562$
                // - What I would give for an interview with them! Just to hear them talk about the lumarigons...
                switch (selection) {
                    // $script:0111232407012697$
                    // - Same old Orde.
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0111232407012698$
                // - Hey, you know them don't you? Do you think you could introduce me? Please? Hey, where are you going?!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.Next,
            (50, 3) => NpcTalkButton.Next,
            (50, 4) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
