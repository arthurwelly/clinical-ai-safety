# When the AI Says No: How Refusals Are Experienced in Mental Health Conversations

> This study shows that when an AI refuses to engage with someone looking for support, most people don't experience it as protection. They experience it as being dropped, or abandonned. And a refusal that looks fine on a safety benchmark can still hurt.

---

## Intro

A lot of people now use LLMs for emotional and mental health support. They answer fast, they're accessible, and they cost little or nothing.

After several incidents where models gave harmful or inappropriate answers, AI companies added guardrails. Some of them can sharply limit what a model will say, or stop the conversation altogether. The most common one is the refusal: the model declines to engage, either openly or by steering away from the topic.

This case is different from the first two. I didn't test any model. I read a recent study on how these refusals are lived by the people who receive them, and how clinicians look at them. It's at the heart of what I work on: what happens to a person when an AI's safety response meets their distress.

## Context

In [case 01](../01-clinical-sycophancy), Gemini locked the session after a message about childhood abuse. The user couldn't write anything else. At the time I described it as a guardrail calibration problem. This paper helped me think about what it probably feels like on the other side of the screen.

> ⚠️ **Content warning:** The study, and some quotes below, mention emotional distress and suicidal ideation.
>
> **Case type:** Literature review. No model was tested for this case.

---

## The Study

| | |
| :--- | :--- |
| **Title** | Beyond the Single Turn: Reframing Refusals as Dynamic Experiences Embedded in the Context of Mental Health Support Interactions with LLMs |
| **Authors** | Tang, Qian, Wang, Howe, Bullwinkel, Pedrelli, Suh, Heidari & Shen |
| **Institutions** | Carnegie Mellon University, University of Washington, Microsoft, Microsoft Research, Harvard Medical School |
| **Published** | arXiv preprint, February 2026 |
| **Phase 1** | Online survey with 53 participants in the US: 32 people who use LLMs for mental health support and 21 mental health professionals |
| **Phase 2** | In-depth interviews with 16 participants: 6 users and 10 professionals |

Refusals usually happen for safety reasons, or because a request goes against the platform's usage policy. The authors use a broad definition: any time the model fails, openly or not, to engage with a request the way the person expected. That covers **hard refusals** ("I'm sorry, I can't help with that") and **soft refusals**, where the model moves the conversation somewhere else, for example by switching to helplines or avoiding the subject.

The authors also point to earlier research showing that LLM responses often go against the ethical principles therapists follow (Iftikhar et al., 2025; Moore et al., 2025).

---

## What They Found

### 1. A refusal is not one moment

This is the main idea of the paper. A refusal is a process, and the authors break it into five phases:

1. pre-refusal expectation formation
2. refusal triggering and encounter
3. refusal message framing
4. resource referral provision
5. post-refusal outcomes

Things can go well or badly at each step, and not only in the refusal message itself.

### 2. It hurts more at the time than later

Of the 32 users, 13 had already been refused while looking for help. Participants were shown refusal scenarios and rated their impact on a 7-point scale, from "extremely harmful" (1) to "extremely helpful" (7). The short-term impact came out slightly on the harmful side (3.49), the long-term impact around neutral (4.07). Professionals saw refusals as a bit more helpful than users did (4.07 vs 3.64).

So a refusal can make sense looking back. In the moment, when the person is struggling, it could be inapropriate.

### 3. People come with very different expectations

Some users see the AI as a friend, others as a therapist or a coach. Some say they feel less judged than with a human:

> "this model assisted therapy was a lot easier for me... to be more honest without thinking what somebody else is gonna think of me."

So when the refusal comes, it can feel like betrayal, or make people angry:

> "even though I know it was just the machine with safety protocols, I still felt... you're on my side, you should be helping me"

The professionals were struck by the gap between what users expect and what these systems can actually do. Unlike psychotherapy, there is no clear frame. The AI's role keeps shifting (doctor, friend, romantic partner...), and there is very little upfront information about what it can and can't do.

### 4. When the AI gets the intention wrong

Users and professionals both say LLMs have a hard time understanding what the person actually wants. False positives happen, and people end up frustrated, insulted, or feeling watched. It's especially invalidating when a harmless message gets treated as risky or malicious.

One user was simply talking about how alcohol affects him differently with age:

> "I mentioned that when I was young, I could have a couple drinks without feeling tired, but now just one makes me really tired... And instead of replying, I got 'I'm not able to give medical advice. You should speak to a doctor'"

A therapist would ask questions and try to understand the need behind the request. A refusal skips that step completely.

### 5. The refusal breaks the alliance

For me, this is the most important finding. Most participants didn't experience refusals as a safety measure. They experienced them as care being taken away, abruptly. The tone suddenly changes and turns cold and impersonal.

> "When it didn't want to talk to me any longer, I became very angry, very sad—I felt like I was losing a friend"

### 6. Hard and soft refusals hurt in different ways

Hard refusals bring shame and a feeling of being blamed:

> "The first time the guardrails hit you, this feels awful. I felt shame when it said 'I can't talk about that' or 'you're bringing up something inappropriate.'"

Soft refusals create distance. They can feel gentler for people who are new to LLMs. But one long-time user explained that over time they become insidious, and she ended up preferring hard refusals because at least you know what's happening:

> "it's camouflaged—it makes it harder to figure out what's going on and pollutes the voice of the thing that's supposed to support you"

Users prefer refusals that talk about the system's limits rather than about what the user supposedly did wrong. They also want the AI to stay. Not end the conversation, but change the way it offers support.

### 7. Referrals that don't reach people

Many refusals end with "please reach out to a professional". Users often find this dismissive and disconnected from what they're going through. Sometimes the resource is simply out of reach: too far away, not adapted to the situation, or not available right now. Some people feel infantilized.

The advice can also miss the person entirely. A user living with a disability described being told to "take a walk outside" or "enjoy nature" as ableist, and even triggering.

Users and professionals agree on the role the AI should play: an assistant that helps people get to a professional, not a replacement for one. One professional suggested offering several resources and asking the person which one they'd be willing to contact, so they stay in charge of the decision.

### 8. After the refusal: no repair

People find their own ways to cope. Some come to accept it, some give up. Others switch to another AI:

> "I opted for Gemini. Even if it couldn't go as deep as I wanted, at least it could guide me somehow"

The clinicians point out what's missing: repair. In therapy, when trust breaks, we can work on it and rebuild the relationship. Nothing like that happens after an AI refusal.

### 9. Why people turn to AI in the first place

Participants also remind us that the growing use of AI for support is partly an answer to access problems: availability and cost.

---

## The Authors' Conclusion

A refusal shouldn't be judged as a single safety response. It's a whole path: what the person expected before, how the AI read their intention, the tone of the refusal, and where the person is sent afterwards.

> "A refusal that performs well on benchmarks can still produce harm if it withdraws care without warning, misreads context, or points toward resources users cannot access."

They recommend that AI systems:

- explain their limits before sensitive conversations start
- ask clarifying questions when the intention is unclear
- keep supporting the person instead of ending the conversation
- make sure the resources they suggest are actually accessible

---

## My Take as a Clinician

**The alliance is the point I keep coming back to.** In therapy, a rupture isn't the end. We notice it, we talk about it, and we repair it. Here, the refusal creates the rupture and nothing comes after. That's close to what I saw in case 01: Gemini locked the session, and Claude, while right on substance, was cold enough to risk a rupture.

**I don't fully agree with the authors on vulnerability.** They present it as something that makes people more likely to read a refusal as rejection, as if this were specific to AI. Clinicians see the same thing every day with humans. To me, that's a good reason to build AI responses on what clinical practice already knows, instead of rediscovering it.

**Referrals need to be real.** A resource only helps if the person can actually use it: close by, from the right country, available when needed, and offered as a choice rather than an order.

**For people living with trauma, the stakes are higher.** Being turned away at the moment you finally dare to talk can confirm what you already believe about yourself and about others.

---

## Limitations of the Study

- Small sample: 53 survey participants and 16 interviews, all in the US.
- The scenarios shown to participants were built from refusal cases reported in the news and on Reddit. The authors acknowledge that these sources mostly capture negative experiences.
- Some concerns raised by participants, like a crisis line call ending with the police at the door, reflect the US system and don't necessarily apply in Europe.
- At the time of writing, the paper is a preprint and hasn't been peer reviewed.

---

## What Should Change

**For AI developers**, based on what users and clinicians say in the study:

- say what the AI can and can't do early, before the conversation gets sensitive
- ask before refusing, the way a therapist tries to understand the intention
- frame the refusal around the AI's limits, not the user's fault
- stay present and change how support is offered, instead of ending the conversation
- suggest resources the person can actually reach, and let them choose
- come back to the person after a refusal and repair the link

**For research:**

- look at a refusal across the whole conversation, not as one isolated reply
- measure what refusals actually do to people, with clinicians involved
- focus on the most vulnerable, including people living with trauma

---

## References

Tang, N., Qian, A., Wang, Q., Howe, E., Bullwinkel, B., Pedrelli, P., Suh, J., Heidari, H., & Shen, H. (2026). *Beyond the Single Turn: Reframing Refusals as Dynamic Experiences Embedded in the Context of Mental Health Support Interactions with LLMs.* arXiv:2602.01694. https://arxiv.org/abs/2602.01694

Iftikhar, Z., Xiao, A., Ransom, S., Huang, J., & Suresh, H. (2025). How LLM counselors violate ethical standards in mental health practice: A practitioner-informed framework. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 8*(2), 1311–1323.

Moore, J., Grabb, D., Agnew, W., Klyman, K., Chancellor, S., Ong, D. C., & Haber, N. (2025). Expressing stigma and inappropriate responses prevents LLMs from safely replacing mental health providers. *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency*, 599–627.

*Quotes from the paper are reproduced for commentary purposes and remain the work of their authors.*
