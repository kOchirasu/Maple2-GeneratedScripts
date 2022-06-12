using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001671: Junta
/// </summary>
public class _11001671 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0711210007006721$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006884$
                // - If you have something to say, just say it.
                switch (selection) {
                    // $script:0727223007006885$
                    // - Where have you been?
                    case 0:
                        return 40;
                    // $script:0727223007006886$
                    // - You're hurt.
                    case 1:
                        return 50;
                    // $script:0727223007006887$
                    // - What are these shadows?
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006888$
                // - As I said, I saw one of those creatures while checking on the barrier stones. It led me into a trap, which took time to get myself out of. Do not worry... those who laid the trap will be laying no others.
                switch (selection) {
                    // $script:0727233607006924$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0727223007006889$
                // - Do not presume to tell me my business! I am the first student of Guidance, and those frail things could hardly lay a... a... whatever they have on me!
                switch (selection) {
                    // $script:0727233607006925$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (60, 0):
                // $script:0727223007006890$
                // - I have no idea. They aren't of nature, that much is obvious. And they are organized. Someone is behind this...
                switch (selection) {
                    // $script:0727233607006926$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
