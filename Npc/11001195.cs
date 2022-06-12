using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001195: Pat
/// </summary>
public class _11001195 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004194$
    // - This place is dry, hot, and unbearably loud. It is absolutely <i>the worst</i>. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004197$
                // - I must've been out of my mind when I agreed to come here. Hmm? And just who are you supposed to be? Wait, did my wise little owl send here?
                switch (selection) {
                    // $script:1016202007004198$
                    // - Your what?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004200$
                // - I'm talking about my beautiful muse! The brains behind our Educational programming, Joanna, of course. <i>Whooo</i>~ else?
                switch (selection) {
                    // $script:1016210507004215$
                    // - But what was that with the owl thing?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1016202007004201$
                // - Owls are smart. It's just a cute nickname, honey. Get over yourself. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
