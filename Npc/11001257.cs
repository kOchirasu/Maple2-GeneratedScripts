using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001257: Moren
/// </summary>
public class _11001257 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 30
    }

    // Select 0:
    // $script:1203001410001288$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:1203001410001290$
                // - You said you wanted me to send you where $npcName:11001229[gender:0]$ went, right? Well, that would be an inn on Victoria Island, in the city of Tria. Would you like to go there now?
                return -1;
            case (30, 0):
                // $script:1203001410001294$
                // - Ever wish you could get somewhere instantaneously? What would you say if I told you I could use a bit of rune magic to send you wherever you want in the blink of an eye?
                switch (selection) {
                    // $script:1203001410001295$
                    // - Please teleport me!
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1203001410001296$
                // - You won't believe it 'til it happens! Oh. Um... just a moment. Uh, it seems I don't have enough rune energy on-hand for the teleportation spell.
                return 31;
            case (31, 1):
                // $script:1203001410001297$
                // - Hmm. You still have things left to do here anyway, don't you? Maybe you should take care of those. I'm not stalling!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.TakeBoat,
            _ => NpcTalkButton.None,
        };
    }
}
